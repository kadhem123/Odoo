from odoo import models, fields

class KevolPassager(models.Model):
    _name = 'kevol.passager'
    _rec_name = 'name'
    name = fields.Char('Nom passager')
    prenom = fields.Char('PreNom passager')
    dateNaissance = fields.Date('Date naissance')
    telephone = fields.Char('téléphone')
    statut = fields.Char('statut')
    def name_get(self):
        result = []
        for passager in self:
            name = passager.name + ' '+ passager.prenom
            result.append((passager.id, name))
            return result

    vol_id = fields.Many2one(comodel_name='kevol.vol')
