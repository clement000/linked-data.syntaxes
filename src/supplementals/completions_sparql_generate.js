
const completions = (s_type, h_prefixes) => JSON.stringify({
	scope:`meta.clause.dataset.rqg`,
	completions: Object.entries(h_prefixes).reduce((a_completions, [s_namespace, p_iri]) => [
		...a_completions,
		{
			trigger: `${s_namespace}:`,
			contents: omar(s_namespace, p_iri),//`${s_namespace}: <${p_iri}>${'at' === s_type? ' .': ''}\n`,
		},
	], []),
}, null, '\t');

const omar= (s_namespace, p_iri) => JSON.stringify({
	scope:`storage.type.prefix.sparql.rqg`,
	completions: 
		{
			navigation: `meta.prologue.rqg`,
			contents: p_iri,//`${s_namespace}: <${p_iri}>${'at' === s_type? ' .': ''}\n`,
		},
}, null, '\t');

// consume prefix context from stdin
let s_prefixes_jsonld = '';
process.stdin.setEncoding('utf8');
process.stdin
	.on('data', (s_chunk) => {
		s_prefixes_jsonld += s_chunk;
	})
	.on('end', () => {
		// prefix-declaration type
		let s_type = process.argv[2] || 'sparql';

		// json-ld (and its context)
		let g_jsonld = JSON.parse(s_prefixes_jsonld);
		let h_prefixes = g_jsonld['@context'];

		// build syntax
		process.stdout.write(completions(s_type, h_prefixes));
	});
