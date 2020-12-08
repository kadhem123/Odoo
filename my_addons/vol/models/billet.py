from odoo import models, fields

class VolBillet(models.Model):
    _name = 'vol.billet'
    date_emission = fields.Datetime('Date Emission')
    date_réservation = fields.Datetime('Date Réservation')
    date_paiement = fields.Datetime('Date Paiement')
