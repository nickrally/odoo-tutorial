from odoo import models
import base64
import io

class PatientCardXlsx(models.AbstractModel):
    _name =  'report.om_hospital.report_patient_id_card_xls'    # follow this format: 'report.module_name.report_name'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):   # will be executed on clicking print button
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})

        for obj in patients:
            sheet = workbook.add_worksheet(obj.name)
            sheet.set_column('D:D', 12)
            sheet.set_column('E:E', 20)
            row = 3
            col = 3

            row += 1
            sheet.merge_range(row, col, row, col + 1, 'ID Card', format_1)

            row += 1
            if obj.image:
                patient_photo = io.BytesIO(base64.b64decode(obj.image))
                sheet.insert_image(row, col, "image.png", {'image_data':patient_photo, 'x_scale':0.5, 'y_scale': 0.5})
                row += 5
            row += 1
            sheet.write(row, col, 'Name', bold)
            sheet.write(row, col+1, obj.name)
            row += 1
            sheet.write(row, col, 'Age', bold)
            sheet.write(row, col+1, obj.age)
            row += 1
            sheet.write(row, col, 'Reference', bold)
            sheet.write(row, col+1, obj.ref)

            row += 2  # gap of two rows between records