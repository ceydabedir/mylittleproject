# SPDX-FileCopyrightText: © 2026 Ceyda Bedir
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Test basliyor...")

    # Saat sinyalini baslat (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset islemi
    dut._log.info("Resetleniyor...")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 5)

    dut._log.info("Mantik kapilari test ediliyor...")

    # SENARYO 1: Input A=1, Input B=1 (ui_in = 3)
    dut.ui_in.value = 3 
    await ClockCycles(dut.clk, 1)
    # Beklenen: AND=1 (uo[0]), OR=1 (uo[1]), XOR=0 (uo[2]) -> Binary: 011 (Decimal 3)
    assert dut.uo_out.value == 3
    dut._log.info("Senaryo 1 (1&1) Basarili!")

    # SENARYO 2: Input A=1, Input B=0 (ui_in = 1)
    dut.ui_in.value = 1
    await ClockCycles(dut.clk, 1)
    # Beklenen: AND=0, OR=1, XOR=1 -> Binary: 110 (Decimal 6)
    assert dut.uo_out.value == 6
    dut._log.info("Senaryo 2 (1&0) Basarili!")

    # SENARYO 3: Input A=0, Input B=0 (ui_in = 0)
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 1)
    # Beklenen: Hepsi 0
    assert dut.uo_out.value == 0
    dut._log.info("Senaryo 3 (0&0) Basarili!")

    dut._log.info("Tebrikler Ceyda! Tum mantik testleri gecti.")
