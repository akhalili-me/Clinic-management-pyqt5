from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,PageBreak
from reportlab.lib.units import cm
from bidi.algorithm import get_display
from arabic_reshaper import reshape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.enums import TA_LEFT
import textwrap
import os
from utility import RESOURCES_DIR, Dates, Numbers


PDF_DIR = RESOURCES_DIR / "pdf"
pdfmetrics.registerFont(TTFont('Vazirmatn', f'{PDF_DIR}/Vazirmatn-Regular.ttf'))
pdfmetrics.registerFont(TTFont('B Titr', f'{PDF_DIR}/B-titr.ttf'))

def rtl_text(text, style,max_line_length=65):
    if len(str(text)) == 0:
        return "-"

    lines = textwrap.wrap(str(text), max_line_length)
    reshaped_lines = [get_display(reshape(line)) for line in lines]
    reshaped_text = '<br/>'.join(reshaped_lines)
    return Paragraph(Numbers.english_to_persian_numbers(reshaped_text), style)

def line():
    line_drawing = Drawing(515, 1)
    line = Line(-5, 0, 515, 0)
    line.strokeColor = colors.HexColor("#2a5d8c")
    line.strokeWidth = 0.01
    line_drawing.add(line)
    return line_drawing


main_title_style = ParagraphStyle(
    'Title',
    fontName='B Titr',
    fontSize=14,
    alignment=2,
    spaceAfter=12,
    textColor=colors.HexColor("#2a5d8c")
)
table_title_style = ParagraphStyle('Title', fontName='B Titr', fontSize=13, alignment=1, spaceAfter=14)
vazirmatn_center = ParagraphStyle("regular", fontName="Vazirmatn", fontSize=12, alignment=1, spaceAfter=14)
vazirmatn_left = ParagraphStyle("JustifyText", fontName="Vazirmatn", fontSize=11, alignment=TA_LEFT, spaceAfter=14,  leftIndent=25)
multi_line_text_styles = ParagraphStyle("regular", fontName="Vazirmatn", fontSize=12, alignment=1, spaceAfter=14, leading=17)


def column_table_style(data):
    col_widths = [523 * 0.8, 523 * 0.2]
    table = Table(data, colWidths=col_widths)
    for row in range(len(data)):
        table.setStyle(TableStyle([('BACKGROUND', (0, row), (-1, row), colors.whitesmoke if row % 2 == 0 else colors.white)]))
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Vazirmatn'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    return table

def header_row_table(data):
    col_widths = [523 / 4] * 4
    table = Table(data, colWidths=col_widths)
    for row in range(len(data)):
        table.setStyle(TableStyle([('BACKGROUND', (0, row), (-1, row), colors.whitesmoke if row % 2 == 0 else colors.white)]))
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Vazirmatn'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        
    ]))
    return table






# Define the total height needed for the approval section
APPROVAL_SECTION_HEIGHT = (
    1.5 * cm  # Approximate height for title and line
    + 0.5 * cm  # Spacer
    + 2 * cm  # Text image height
    + 0.5 * cm  # Spacer for label
    + 2.5 * cm  # Signature image height
)

# Define the page height in points
PAGE_HEIGHT = 29.7 * cm  # A4 height


def add_approval_section(elements, patient_data):
    """Adds the approval section, moving to the next page if necessary."""
    
    # Track whether a page break was added by this section
    page_break_added = False

    # Calculate the current Y position on the page
    current_y_position = sum(element.wrap(PAGE_HEIGHT, PAGE_HEIGHT)[1] for element in elements)

    # Check if the remaining space can fit the approval section
    if current_y_position + APPROVAL_SECTION_HEIGHT > PAGE_HEIGHT:
        elements.append(PageBreak())  # Move to a new page if not enough space
        page_break_added = True  # Indicate that a page break was added

    # Add Approval Section Title and Line
    elements.append(rtl_text("رضایت‌نامه", main_title_style))
    elements.append(line())
    elements.append(Spacer(1, 12))

    # Add the Text Image
    text_image = Image(f"{PDF_DIR}/text.jpg", width=18.3 * cm, height=2 * cm)
    text_image.hAlign = 'CENTER'
    elements.append(text_image)
    elements.append(Spacer(1, 6))

    # Add Signature Label
    elements.append(rtl_text("امضاء بیمار", vazirmatn_left))

    # Add Signature Image if it exists
    if os.path.exists(patient_data["signature"]):
        signature_image = Image(patient_data["signature"], width=3.5 * cm, height=2.5 * cm)
        signature_image.hAlign = "LEFT"
        elements.append(signature_image)

    return page_break_added  # Return whether a page break was added




def create_patient_file_pdf(patient_data, medical_records, file_directory):
    file_name = f'{file_directory}/{patient_data["firstName"]} {patient_data["lastName"]}.pdf'
    pdf = SimpleDocTemplate(
        file_name, pagesize=A4,
        rightMargin=1.27 * cm, leftMargin=1.27 * cm,
        topMargin=0.1 * cm, bottomMargin=1.27 * cm
    )
    elements = []

    # Header - Logo
    logo_image = Image(f"{PDF_DIR}/logo.png", width=3 * cm, height=3 * cm)
    logo_image.hAlign = 'CENTER'
    elements.append(logo_image)

    # Personal Information Section
    elements.append(rtl_text("اطلاعات شخصی", main_title_style))
    elements.append(line())
    elements.append(Spacer(1, 12))

    # Personal Information Table
    personal_info = [
        [rtl_text(patient_data["id"], vazirmatn_center), rtl_text("شماره پرونده", table_title_style)],
        [rtl_text(patient_data["firstName"], vazirmatn_center), rtl_text("نام بیمار", table_title_style)],
        [rtl_text(patient_data["lastName"], vazirmatn_center), rtl_text("نام خانوادگی", table_title_style)],
        [rtl_text(patient_data["identityCode"], vazirmatn_center), rtl_text("کد ملی", table_title_style)],
        [rtl_text(patient_data["age"], vazirmatn_center), rtl_text("سن", table_title_style)],
        [rtl_text(patient_data["phoneNumber"], vazirmatn_center), rtl_text("شماره تلفن", table_title_style)],
        [rtl_text(patient_data["job"], vazirmatn_center), rtl_text("شغل", table_title_style)],
        [rtl_text(patient_data["maritalStatus"], vazirmatn_center), rtl_text("وضعیت تاهل", table_title_style)],
        [rtl_text(patient_data["pregnant"], vazirmatn_center), rtl_text("باردار", table_title_style)],
        [rtl_text(patient_data["address"], multi_line_text_styles), rtl_text("آدرس", table_title_style)],
        [rtl_text(patient_data["extraInfo"], multi_line_text_styles), rtl_text("اطلاعات اضافه", table_title_style)],
    ]
    elements.append(column_table_style(personal_info))
    elements.append(Spacer(1, 15))

    # Allergies and Conditions Section
    elements.append(rtl_text("وضعیت‌ بیمار", main_title_style))
    elements.append(line())
    elements.append(Spacer(1, 12))

    patient_conditions = [
        [rtl_text(patient_data["allergy"], multi_line_text_styles), rtl_text("حساسیت‌ها", table_title_style)],
        [rtl_text(patient_data["disease"], multi_line_text_styles), rtl_text("بیماری‌ها", table_title_style)],
        [rtl_text(patient_data["medication"], multi_line_text_styles), rtl_text("داروها", table_title_style)],
        [rtl_text(patient_data["specialCondition"], vazirmatn_center), rtl_text("وضعیت خاص بیمار", table_title_style)],
    ]
    elements.append(column_table_style(patient_conditions))
    elements.append(Spacer(1, 15))

    # # Approval Section
    # elements.append(rtl_text("رضایت‌نامه", main_title_style))
    # elements.append(line())
    # elements.append(Spacer(1, 12))

    # text_image = Image(f"{PDF_DIR}/text.jpg", width=18.3 * cm, height=2 * cm)
    # text_image.hAlign = 'CENTER'
    # elements.append(text_image)
    # # elements.append(Spacer(1, 12))

    # elements.append(rtl_text("امضاء بیمار", vazirmatn_left))

    # if os.path.exists(patient_data["signature"]):
    #     signature_image = Image(patient_data["signature"], width=3.5 * cm, height=2.5 * cm)
    #     signature_image.hAlign = "LEFT"
    #     elements.append(signature_image)

    # elements.append(PageBreak())

    approval_page_break = add_approval_section(elements, patient_data)

    # Add Appointment Records Section, adding a PageBreak only if no page break was added earlier
    if not approval_page_break:
        elements.append(PageBreak())

    # Appointment Records Section
    elements.append(rtl_text("خدمات ارائه شده", main_title_style))
    elements.append(line())
    elements.append(Spacer(1, 12))

    medical_records_data = [
        [
            rtl_text("مبلغ", table_title_style),
            rtl_text("دکتر", table_title_style),
            rtl_text("سرویس", table_title_style),
            rtl_text("تاریخ", table_title_style),
        ]
    ] + [
        [
            rtl_text(
                f"{Numbers.int_to_persian_with_separators(record["price"])} تومان",
                vazirmatn_center,
            ),
            rtl_text(record["doctor_name"], vazirmatn_center),
            rtl_text(record["service_name"], vazirmatn_center),
            rtl_text(
                Dates.convert_to_jalali_format(record["jalali_date"]), vazirmatn_center
            ),
        ]
        for record in medical_records
    ]
    elements.append(header_row_table(medical_records_data))

    pdf.build(elements)
