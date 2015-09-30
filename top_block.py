#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Sep 29 19:25:48 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 5e6
        self.freqScan = freqScan = 100.5e6
        self.freqC = freqC = 100.5e6
        self.fftSize = fftSize = 512
        self.decimation = decimation = 20

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "RF Spectrum")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "RF Waterfall")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Demod")
        self.Add(self.notebook_0)
        _freqC_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freqC_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freqC_sizer,
        	value=self.freqC,
        	callback=self.set_freqC,
        	label='freqC',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freqC_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freqC_sizer,
        	value=self.freqC,
        	callback=self.set_freqC,
        	minimum=87.7e6,
        	maximum=107.7e6,
        	num_steps=int((107.7-87.7)*10/2.0+1),
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freqC_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	baseband_freq=freqC,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=fftSize,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(2).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(2).Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	baseband_freq=freqC,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=fftSize,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freqC, 0)
        self.uhd_usrp_source_0.set_gain(25, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(48e3),
                decimation=int(samp_rate/decimation),
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(decimation, firdes.low_pass(
        	1, samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        _freqScan_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freqScan_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freqScan_sizer,
        	value=self.freqScan,
        	callback=self.set_freqScan,
        	label='freqScan',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freqScan_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freqScan_sizer,
        	value=self.freqScan,
        	callback=self.set_freqScan,
        	minimum=87.7e6,
        	maximum=107.7e6,
        	num_steps=int((107.7-87.7)*10/2.0+1),
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freqScan_sizer)
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate/decimation,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.wxgui_fftsink2_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_waterfallsink2_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)

    def get_freqScan(self):
        return self.freqScan

    def set_freqScan(self, freqScan):
        self.freqScan = freqScan
        self._freqScan_slider.set_value(self.freqScan)
        self._freqScan_text_box.set_value(self.freqScan)

    def get_freqC(self):
        return self.freqC

    def set_freqC(self, freqC):
        self.freqC = freqC
        self._freqC_slider.set_value(self.freqC)
        self._freqC_text_box.set_value(self.freqC)
        self.uhd_usrp_source_0.set_center_freq(self.freqC, 0)
        self.wxgui_fftsink2_0.set_baseband_freq(self.freqC)
        self.wxgui_waterfallsink2_0.set_baseband_freq(self.freqC)

    def get_fftSize(self):
        return self.fftSize

    def set_fftSize(self, fftSize):
        self.fftSize = fftSize

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
