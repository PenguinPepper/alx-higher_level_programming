$(function ()
{
	url = "https://swapi-api.alx-tools.com/api/films/?format=json";
	$.get(url, funtion(data, textstatus)
	{
		$("DIV#character").html(`<div id="character">${data.name}</div>`);
});
