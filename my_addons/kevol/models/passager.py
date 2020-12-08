from odoo import models, fields

class KevolPassager(models.Model):
    _name = 'kevol.passager'
    nom = fields.Char('Nom passager')
    prenom = fields.Char('PreNom passager')
    date_naissance = fields.Date('Date naissance')
    telephone = fields.Char('téléphone')
    statut = fields.Char('statut')
