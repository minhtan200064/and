module tt_um_example (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Không dùng các chân này
    wire _unused = &{ena, clk, rst_n, uio_in};

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Cổng AND 2 ngõ vào
    assign uo_out[0] = ui_in[0] & ui_in[1];

    // Các output còn lại bằng 0
    assign uo_out[7:1] = 7'b0000000;

endmodule
