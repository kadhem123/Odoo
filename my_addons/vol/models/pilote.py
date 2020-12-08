from odoo import models, fields

class VolPilote(models.Model):
    _name = 'vol.pilote'
    nom = fields.Char('Nom Pilote')
    prenom = fields.Char('Prénom Pilote')
    qualif = fields.Char('Qualifications')
