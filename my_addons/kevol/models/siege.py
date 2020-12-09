from odoo import models, fields

class Kevolsiege(models.Model):
    _name = 'kevol.siege'
    numAllee = fields.Char('num allée')
    numRang = fields.Char('numero rang')
    classe = fields.Char('Classe')
    avion_id = fields.Many2one(comodel_type='kevol.avion')

