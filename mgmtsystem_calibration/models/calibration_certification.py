# Copyright 2020 Escodoo (<https://escodoo.com.br>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class MgmtsystemCalibrationCertification(models.Model):
    """Main control for certifications on equipment calibrations."""

    _name = 'mgmtsystem_calibration.certification'
    _description = "Certification Control for Equipment Calibrations (Metrology)"

    name = fields.Char('Certification Identification', required=True)

    certificationtype_id = fields.Many2one('mgmtsystem_calibration.certificationtype',
                                  string='Certification Type',
                                  required=True)

    equipment = fields.Char('Equipment Model', 
                                help="Equipment model")

    serial_number = fields.Char('Serial Number', 
                                help="Equipment serial number. Must be unique.")
    is_client_equipment = fields.Boolean("Is it a client's equipment?", 
                                help="Check this box if the equipment belongs to a third party.")
    client_id = fields.Many2one('res.partner',
                                 'Client',
                                 help="Partner who owns the equipment")
    service_order_number  = fields.Char('Service Order #', 
                                help="When applicable, type the service order number.")
    calibration_date = fields.Date('Calibration Date')
    valid_to_date = fields.Date('Expiry Date')

    issuer_id = fields.Many2one('res.partner',
                                 'Issued By',
                                 help="Partner who issues de certificate")

    additional_notes = fields.Text('Additional Notes')
    