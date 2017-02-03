odoo.define('ncf_do_pos.main', function (require) {
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

  return {
    Mine: mine
  };
});
