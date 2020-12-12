from odoo import models, fields

class KevolPilote(models.Model):
    _name = 'kevol.pilote'
    name = fields.Char('Nom Pilote')
    prenom = fields.Char('Prénom Pilote')
    qualif = fields.Char('Qualifications')
    compagnie_id = fields.Many2one(comodel_name='kevol.compagnie')
    avion_id = fields.Many2one(comodel_name='kevol.avion')
    def name_get(self):
        result = []
        for passager in self:
            name = passager.name + ' ' + passager.prenom
            result.append((passager.id, name))
            return result



