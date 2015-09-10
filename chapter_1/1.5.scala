/* 
 	CCC 1.4: Given a string, compress it into a sparce vector
 	If no compression, return the regular string
 	e.g. aabbaaac = a2b2a3c
*/

def replace_solution(s: String): String = {
	s.replaceAll("\\s", "%20")
}

println(replace_solution("a b  c"))