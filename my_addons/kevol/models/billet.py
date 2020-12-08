from odoo import models, fields

class KevolBillet(models.Model):
    _name = 'kevol.billet'
    date_emission = fields.Datetime('Date Emission')
    date_reservation = fields.Datetime('Date Réservation')
    date_paiement = fields.Datetime('Date Paiement')
