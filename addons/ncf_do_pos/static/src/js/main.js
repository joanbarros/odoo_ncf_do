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

  return {
    Mine: mine
  };
});
