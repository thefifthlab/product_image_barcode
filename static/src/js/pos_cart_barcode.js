/** @odoo-module **/

import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { patch } from "@web/core/utils/patch";

patch(Orderline.prototype, {
    setup() {
        super.setup();
    },

    get barcode() {
        return this.props.line.product?.barcode || '';
    },
});

// Safer DOM injection
const originalSetup = Orderline.prototype.setup;
Orderline.prototype.setup = function () {
    originalSetup.call(this);

    // Use Owl's onMounted hook if available, fallback to timeout
    if (this.env && this.env.__owl__) {
        // For newer Owl
        this.env.__owl__.onMounted(() => this._addBarcode());
    } else {
        setTimeout(() => this._addBarcode(), 80);
    }
};

Orderline.prototype._addBarcode = function () {
    const el = this.__owl__?.el || this.el;
    if (!el || !this.barcode) return;

    // Clean previous barcodes
    el.querySelectorAll('.custom-barcode').forEach(e => e.remove());

    const div = document.createElement('div');
    div.className = 'custom-barcode';
    div.style.cssText = `
        font-size: 10.5px;
        color: #555;
        font-family: monospace;
        margin-top: 4px;
        text-align: left;
    `;
    div.textContent = this.barcode;

    // Insert after product info
    const target = el.querySelector('.product-name, .info, .qty, .price')?.parentElement || el;
    target.appendChild(div);
};