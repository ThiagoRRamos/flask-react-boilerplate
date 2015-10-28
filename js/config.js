require.config({
	baseUrl: "/static/js",
	paths: {
      'jquery': '/static/v/jquery/dist/jquery.min',
      'react': '/static/v/react/react',
      'markdown': '/static/v/markdown/lib/markdown',
      'katex': '/static/v/katex-build/katex.min',
      'flux': '/static/v/flux/dist/Flux',
      'mousetrap': '/static/v/mousetrap-min/mousetrap.min',
      'reactchart': '/static/v/react-chartjs/react-chartjs',
      'Chartjs': '/static/v/chartjs/Chart'
    },
    shim: {
	    markdown: {
	    	exports: "exports",
	    	init: function() {
	    		return markdown;
	    	}
	    }
	}
})