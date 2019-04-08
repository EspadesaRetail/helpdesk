# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase, tagged



@tagged('standard', 'nice')
class HelpdeskCase(TransactionCase):
    def setUp(self):
        super(HelpdeskCase, self).setUp()
        self.stage_obj = self.env['helpdesk.stage']
        self.ticket_obj = self.env['helpdesk.ticket']
        self.team_obj = self.env['helpdesk.team']
        self.stage1 = self.stage_obj.create({
            'name': 'stage1'
        })
        self.stage2 = self.stage_obj.create({
            'name': 'stage1'
        })
        self.ticket1 = self.ticket_obj.create({
            'name': 'ticket1'
        })
        self.team1 = self.team_obj.create({
            'name': 'Team1',
            'code': 'code'
        })


    def test_stage_asign(self):
        """Probando asignación de tests.
        """
        self.ticket1.stage_id = self.stage1
        self.assertEqual(self.ticket1.stage_id, self.stage1)
        self.ticket1.stage_id = self.stage2
        self.assertEqual(self.ticket1.stage_id, self.stage2)
        pass

    def test_team_name(self):
        """Probando test name.
        """
        self.ticket1.team_id = self.team1
        data = self.ticket1.read(['team_id'])
        team_name = data[0]['team_id'][1]
        self.assertEqual(team_name, '[code]Team1')
