from odoo import models, fields

class Kevolsiege(models.Model):
    _name = 'kevol.siege'
    numAllee = fields.Char('num allée')
    numRang = fields.Char('numero rang')
    classe = fields.Selection([('Economique', 'Economique'), ('Economique Prenium', 'Economique Prenium'),('Business', 'Business'),('Premiére', 'Premiére')])
    _rec_name = 'classe'
    avion_id = fields.Many2one(comodel_name='kevol.avion')
    billet_id = fields.One2many(comodel_name='kevol.billet',
                             inverse_name='siege_id')

