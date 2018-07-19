import _plotly_utils.basevalidators


class SpikecolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self,
        plotly_name='spikecolor',
        parent_name='layout.scene.zaxis',
        **kwargs
    ):
        super(SpikecolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            **kwargs
        )