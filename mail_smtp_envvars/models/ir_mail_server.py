# Copyright 2023 Ross Golder (https://golder.org)
# Copyright 2022 ForgeFlow S.L. (https://forgeflow.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os

from odoo import api, models
from odoo.exceptions import UserError


class IrMailServer(models.Model):

    _inherit = "ir.mail_server"

    def connect(self, host=None, port=None, user=None, password=None, encryption=None,
                smtp_debug=False, mail_server_id=None):
        if 'SMTP_HOST' not in os.environ:
            raise UserError("Missing 'SMTP_HOST' environment variable")
        smtp_host = os.environ['SMTP_HOST']
        smtp_port = int(os.environ['SMTP_PORT'])
        smtp_user = os.getenv('SMTP_USER', None)
        smtp_password = os.getenv('SMTP_PASSWORD', None)
        smtp_encryption = os.getenv('SMTP_ENCRYPTION', None)
        smtp_debug = int(os.getenv('SMTP_DEBUG', "0"))
        return super().connect(
            smtp_host,
            smtp_port,
            smtp_user,
            smtp_password,
            smtp_encryption,
            smtp_debug,
            None,
        )
