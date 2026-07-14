import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_project(dut):

    dut.ena.value = 1
    dut.rst_n.value = 1
    dut.uio_in.value = 0

    # A=0 B=0
    dut.ui_in.value = 0b00000000
    await Timer(1, units="ns")
    assert int(dut.uo_out.value) == 0

    # A=0 B=1
    dut.ui_in.value = 0b00000010
    await Timer(1, units="ns")
    assert int(dut.uo_out.value) == 0

    # A=1 B=0
    dut.ui_in.value = 0b00000001
    await Timer(1, units="ns")
    assert int(dut.uo_out.value) == 0

    # A=1 B=1
    dut.ui_in.value = 0b00000011
    await Timer(1, units="ns")
    assert int(dut.uo_out.value) == 1
