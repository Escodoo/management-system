# Copyright 2020 Escodoo (<https://escodoo.com.br>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class MgmtsystemCalibrationCertificationType(models.Model):
    """Added the details of the certification types."""

    _name = 'mgmtsystem_calibration.certificationtype'

    name = fields.Char('Certification Type',
                                help='E.g., Equipment Calibration, Electric Safety, etc.')
