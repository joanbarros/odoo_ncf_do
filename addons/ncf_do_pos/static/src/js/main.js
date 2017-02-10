odoo.define('ncf_do_pos.main', function (require) {
  var Model = require('web.DataModel');
  window.posorder = new Model('pos.order');
  console.log('from the new module');
  var pos_screens = require('point_of_sale.screens');
  var mine = pos_screens.NumpadWidget.include({
    clickAppendNewChar: function (event) {
      console.log('from within the NumpadWidget');
      console.log('NumpadWidget debug', this, event);
      this._super(event);
      console.log('finish NumpadWidget');
    }
  });

  // Add the field to the model so it's pulled form the db
  var pos_models = require('point_of_sale.models');
  console.log('pos_models', pos_models);
  var models = pos_models.PosModel.prototype.models;
  for (var i = 0; i < models.length; i++) {
    if (models[i].model == 'res.partner') {
      console.log('fields', models[i].fields);
      models[i].fields.push('rnc');
      console.log('Added rnc field to the partner field list');
    }
  }
  console.log('newPosModel', pos_models.PosModel);

  var export_for_printing = pos_models.Order.prototype.export_for_printing;

  pos_models.Order.prototype.export_for_printing = function () {
    var thisOrder = this;
    var OrderModel = new Model('pos.order');
    var self = this;
    var receipt = null;

    console.log('123 testing');
    console.debug('order', this);
    var order = OrderModel.query(['ncf'])
    //.filter([['pos_reference', '=', thisOrder.name]])
    .order_by(['-create_date'])
    .limit(1)
    .all()
    .then(function (order) {
      receipt = export_for_printing.apply(self, arguments);
      console.debug('fetched order', order);
      // console.debug('receipt', receipt);
      receipt.ncf = order[0].ncf;
      console.debug('receipt', receipt);
      //return receipt;
    });

    // receipt.ncf = 'Test';

    return receipt;
  }

  return {
    Mine: mine
  };
});
