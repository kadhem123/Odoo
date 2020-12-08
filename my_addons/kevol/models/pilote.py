from odoo import models, fields

class KevolPilote(models.Model):
    _name = 'kevol.pilote'
    nom = fields.Char('Nom Pilote')
    prenom = fields.Char('Prénom Pilote')
    qualif = fields.Char('Qualifications')
