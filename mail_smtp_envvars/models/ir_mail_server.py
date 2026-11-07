# Copyright 2023 Ross Golder (https://golder.org)
# Copyright 2022 ForgeFlow S.L. (https://forgeflow.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os

from odoo import api, models
from odoo.exceptions import UserError


class IrMailServer(models.Model):

    _inherit = "ir.mail_server"

    # TODO(18.0-port): the positional super().connect() call below (host, port, user,
    # password, encryption, smtp_debug, None) matches the signature this override was
    # written against. The 18.0 ir.mail_server.connect() signature could not be verified:
    # no core Odoo source and no 18.0 override of ir.mail_server.connect exists in the
    # OpenUpgrade or OCA 18.0 worktrees. Confirm the parameter list in core mail/models/ir_mail_server.py.
    def connect(self, host=None, port=None, user=None, password=None, encryption=None,
                smtp_debug=False, mail_server_id=None, smtp_from=None):
        if 'SMTP_HOST' not in os.environ:
            raise UserError("Missing 'SMTP_HOST' environment variable")
        smtp_host = os.environ['SMTP_HOST']
        smtp_port = int(os.environ['SMTP_PORT'])
        smtp_user = os.getenv('SMTP_USER', None)
        smtp_password = os.getenv('SMTP_PASSWORD', None)
        smtp_encryption = os.getenv('SMTP_ENCRYPTION', None)
        smtp_debug = int(os.getenv('SMTP_DEBUG', "0"))
        
        return super().connect(
            host=smtp_host,
            port=smtp_port,
            user=smtp_user,
            password=smtp_password,
            encryption=smtp_encryption,
            smtp_from=smtp_from,
            smtp_debug=smtp_debug,
            mail_server_id=None,
        )
