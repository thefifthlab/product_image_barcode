import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { patch } from "@web/core/utils/patch";

patch(PosOrderline.prototype, {
    getDisplayData() {
        const result = super.getDisplayData(...arguments);
        result.productBarcode = this.product_id?.barcode || "";
        return result;
    },
});

patch(Orderline.props.line.shape, {
    productBarcode: { type: String, optional: true },
});