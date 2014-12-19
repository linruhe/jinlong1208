
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

class product_query_wizard(osv.osv_memory):

    _name = 'product.query.wizard'
    _description = 'Wizard that opens the product_product table'
    _columns = {
        'choose_date': fields.boolean('Choose a Particular Date'),
        'choose_attribute': fields.boolean('Choose Attributes of products'),
        'date': fields.datetime('Date', required=True),
        'test': fields.char('test'),
		'attribute_line_ids': fields.many2one('product.attribute.value','Attribute_1'),
        'attribute_value_1': fields.many2one('product.attribute.value','Attribute_1'),
        'attribute_value_2': fields.many2one('product.attribute.value','Attribute_2'),
        'attribute_value_3': fields.many2one('product.attribute.value','Attribute_3'),
        'attribute_value_4': fields.many2one('product.attribute.value','Attribute_4'),
        'attribute_value_5': fields.many2one('product.attribute.value','Attribute_5'),
        'attribute_value_6': fields.many2one('product.attribute.value','Attribute_6'),
        'attribute_value_7': fields.many2one('product.attribute.value','Attribute_7'),
        'attribute_value_8': fields.many2one('product.attribute.value','Attribute_8'),
    }

    _defaults = {
        'choose_date': False,
        'choose_attribute': True,
        'date': fields.datetime.now,
    }

    def open_table(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        data = self.read(cr, uid, ids, context=context)[0]
        if data['attribute_line_ids']:
            test =  data['attribute_line_ids'][1]
        else :
            test =''     
        if data['attribute_value_1']:
            value_1 =  data['attribute_value_1'][1]
        else :
            value_1 =''
        if data['attribute_value_2']:
            value_2 =  data['attribute_value_2'][1]
        else :
            value_2 =''
        if data['attribute_value_3']:
            value_3 =  data['attribute_value_3'][1]
        else :
            value_3 =''             
        if data['attribute_value_4']:
            value_4 =  data['attribute_value_4'][1]
        else :
            value_4 =''   
        if data['attribute_value_5']:
            value_5 =  data['attribute_value_5'][1]
        else :
            value_5 =''             
        if data['attribute_value_6']:
            value_6 =  data['attribute_value_6'][1]
        else :
            value_6 ='' 
        if data['attribute_value_7']:
            value_7 =  data['attribute_value_7'][1]
        else :
            value_7 =''             
        if data['attribute_value_8']:
            value_8 =  data['attribute_value_8'][1]
        else :
            value_8 =''             
            
            
                                                         
        ctx = context.copy()
        #ctx['history_date'] = data['date']
        #ctx['search_default_group_by_product'] = True
        #ctx['search_default_group_by_location'] = True
        if data['choose_attribute'] :
            return {
                'domain': "[('attribute_value_ids', 'like', '"+test +"'),('attribute_value_ids', 'like', '"+value_1+"'),('attribute_value_ids', 'like', '"+value_2 +"'),('attribute_value_ids', 'like', '"+value_3 +"'),('attribute_value_ids', 'like', '"+value_4+"'),('attribute_value_ids', 'like', '"+value_5+"'),('attribute_value_ids', 'like', '" +value_6 + "'),('attribute_value_ids', 'like', '" +value_7 + "'),('attribute_value_ids', 'like', '" +value_8 + "')]",
                'name': _('Stock Value At Date'),
                'view_type': 'form',
                'view_mode': 'tree,form,graph',
                'res_model': 'product.product',
                'type': 'ir.actions.act_window',
                'context': ctx,
            }
        else :
            return {
                'domain': "[]",
                'name': _('Stock Value At Date'),
                'view_type': 'form',
                'view_mode': 'tree,form,graph',
                'res_model': 'product.product',
                'type': 'ir.actions.act_window',
                'context': ctx,
            }
