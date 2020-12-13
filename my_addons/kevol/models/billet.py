from odoo import models, fields

class KevolBillet(models.Model):
    _name = 'kevol.billet'
    name=fields.Char('Réf billets')
    dateEmission = fields.Datetime('Date Emission')
    dateReservation = fields.Datetime('Date Réservation')
    datePaiement = fields.Datetime('Date Paiement')
    siege_id = fields.Many2one(comodel_name='kevol.siege')
    vol_id = fields.Many2one(comodel_name='kevol.vol')
    passager_id = fields.Many2one(comodel_name='kevol.passager')





