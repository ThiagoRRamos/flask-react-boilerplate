import React from 'react'
import $ from 'jquery'

var SectionResult = React.createClass({
	goToQuery: function(val){
		window.location = "/search?q=" + val
	},
	render: function(){
		return (
			<div className="col-md-12 search-result pam">
				<h5>{this.props.data.title}</h5>
			</div>
		);
	}
});

var Search = React.createClass({
	getInitialState: function(){
		var query = this.props.query ? this.props.query : '';
		return {query: query, results: []}
	},
	componentDidMount: function() {
		if (this.state.query) {
			this.fetchResults();
		}
	},
	fetchResults: function (){
		$.post('/search/results', {query: this.state.query}, (function(data){
			if (!data.error) {
				this.setState(data.data);
			}
		}).bind(this));
	},
	handleEditQuery: function(evt) {
		this.setState({query: evt.target.value}, this.fetchResults)
	},
	render: function(){
		var sectionResults = this.state.results.slice(0, 10).map(function(a, ind){
			return <SectionResult key={ind} data={a} />;
		})
		return (
			<div className="col-md-10 col-md-offset-1">
				<div className="row mbm">
					<div className="col-md-6 col-md-offset-3">
						<input
							type="text"
							onChange={this.handleEditQuery}
							className="form-control"
							placeholder="Busca"
							value={this.state.query}
						/>
					</div>
				</div>
				<h4>Resultados</h4>
				<div className="row">
					{sectionResults}
				</div>
			</div>
		);
	}
});

export default Search;