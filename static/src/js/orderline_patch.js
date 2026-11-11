/** @odoo-module */

import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { patch } from "@web/core/utils/patch";

patch(Orderline.prototype, {
    setup() {
        super.setup();
        this.barcode = this.env.pos.db.get_product_by_id(this.props.line.productId)?.barcode || "";
    }
});