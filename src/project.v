/*
 * Copyright (c) 2026 Ceyda Bedir
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_ceydabedir (
    input  wire [7:0] ui_in,    // Girişler
    output wire [7:0] uo_out,   // Çıkışlar
    input  wire [7:0] uio_in,   // Giriş/Çıkış pinleri (Giriş yolu)
    output wire [7:0] uio_out,  // Giriş/Çıkış pinleri (Çıkış yolu)
    output wire [7:0] uio_oe,   // Giriş/Çıkış yetki (1=output, 0=input)
    input  wire       ena,      // Tasarım aktif mi? (Genelde 1)
    input  wire       clk,      // Saat sinyali
    input  wire       rst_n     // Reset (Sıfırlama - Low aktif)
);

    // Senin Mantık Devren:
    // ui_in[0] ve ui_in[1] pinlerini kullanıyoruz.
    assign uo_out[0] = ui_in[0] & ui_in[1]; // AND Kapısı
    assign uo_out[1] = ui_in[0] | ui_in[1]; // OR Kapısı
    assign uo_out[2] = ui_in[0] ^ ui_in[1]; // XOR Kapısı
    
    // Kullanılmayan diğer çıkış pinlerini mutlaka 0'a eşitlemelisin:
    assign uo_out[7:3] = 5'b00000;
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Uyarıları engellemek için kullanılmayan girişleri buraya ekliyoruz:
    wire _unused = &{ena, clk, rst_n, ui_in[7:2], uio_in, 1'b0};

endmodule
