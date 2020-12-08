from odoo import models, fields

class Kevolsiege(models.Model):
    _name = 'kevol.siege'
    num_allee = fields.Char('num allée')
    num_rang = fields.Char('numero rang')
    classe = fields.Char('Classe')
