from odoo import models, fields

class VolPassager(models.Model):
    _name = 'vol.passager'
    nom = fields.Char('Nom passager')
    prenom = fields.Char('PreNom passager')
    date_naissance = fields.Date('Date naissance')
    téléphone = fields.Char('téléphone')
    statut = fields.Char('statut')
