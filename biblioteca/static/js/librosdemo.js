$('.button-collapse').sideNav();
var elementoAnterior = 2;
var img = new Array[
    'img/percy1.jpg', 
    'img/percy2.jpg', 
    'img/percy3.jpg', 
    'img/percy4.jpg', 
    'img/percy5.jpg'];
var titulos = new Array[
    'El ladrón del rayo',
    'El mar de los moustros',
    'La maldición del titán',
    'La batalla del laberinto',
    'El último héroe del olimpo'];
var contenido = new Array[
    '¿Qué pasaría si un día descubres que, en realidad, eres hijo de un dios griego que debe cumplir una misión secreta? Pues eso es lo que le sucede a Percy Jackson, que a partir de ese momento se dispone a vivir los acontecimientos más emocionantes de su vida. Expulsado de seis colegios, Percy padece dislexia y dificultades pa ra concentrarse, o al menos ésa es la versión oficial. Objeto de burlas por inventarse historias fantásticas, ni siquiera él mismo acaba de creérselas hasta el día que los dioses del Olimpo le revelan la verdad: Percy es nada menos que un semidiós, es decir, el hijo de un dios y una mortal. Y como tal ha de descubrir quién ha robado el rayo de Zeus y así evitar que estalle una guerra entre los dioses. Para cumplir la misión contará con la ayuda de sus amigos Grover, un joven sátiro, y Annabeth, hija de la sabia Atenea. El ladrón del rayo da comienzo a una apasionante serie de aventuras sobre un mundo secreto, el mundo que los antiguos dioses griegos han recreado a nuestro alrededor en pleno siglo XXI.',
    'Cuando el árbol de Thalía es misteriosamente envenenado, las fronteras mágica del Campamento de los semidioses comienzan a fallar. Ahora Percy y sus amigos tienen unos días para encontrar el único elemento de magia de gran alcance para salvar el campamento antes de que sea invadida por monstruos. Las capturas: deben navegar en el mar de monstruos para encontrarlo. En el camino, Percy debe organizar una audaz operación de rescate para salvar a su viejo amigo Grover, y se entera de un terrible secreto sobre su propia familia, que le hace preguntarse si ser el hijo de Poseidón es un honor o una maldición.',
    'Cuando Percy Jackson recibe una llamada urgente de auxilio de su amigo Grover, de inmediato se prepara para la batalla. Sabe que tendrá sus poderosos aliados semidióses a su lado, su fiel espada de bronce "Riptide", y... un viaje de su mamá. Los semidioses corren al rescate para encontrar que Grover ha hecho un descubrimiento importante: dos mestizos poderosos cuya filiación se desconoce. Pero eso no es todo lo que les espera. El señor titán Kronos ha elaborado su plan aún más traicionero, y los jóvenes héroes acaban de caer como presas. No son los únicos en peligro. Un antiguo monstruo se ha producido - un rumor que a ser tan poderoso podría destruir al Olympo - y Artemisa, la diosa que sólo podría saber cómo realizar un seguimiento, con algo que falta. Ahora, Percy y sus amigos, junto con los cazadores de Artemisa, sólo tienen una semana para encontrar la diosa secuestrada y resolver el misterio del monstruo que estaba buscando.En el camino, deben enfrentar su desafío más peligroso: la profecía de refrigeración de la maldición de Titán.',
    'Percy Jackson no espera que la orientación de primer año sera nada divertido, pero cuando un conocido mortal misterioso aparece, perseguido por porristas demonios, las cosas rápidamente van de mal en peor. El tiempo se agota para Percy. La guerra entre los dioses y los titanes se acerca. Ni siquiera el Campamento para semidioses es seguro, cuando el ejército de Kronos se prepara para invadir sus fronteras, una vez es impenetrable. Para detenerlos, Percy y sus amigos deberán figurar en una búsqueda a través del laberinto - un mundo inmenso en un laberinto subterráneo lleno de sorpresas y peligros a cada paso. En el camino se enfrentará a poderosos enemigos, descubrirá la verdad sobre la pérdida del dios Pan, y el señor Titan descubrira un secreto terrible de Kronos. La guerra final comienza... con la batalla del laberinto.',
    'Los mestizos han dedicado mucho tiempo a prepararse para la batalla decisiva contra los titanes, aunque saben que sus posibilidades de obtener la victoria son mínimas. El ejército de Cronos es ahora más formidable que nunca y, con cada dios y cada mestizo que logra reclutar, aumentan los poderes del maligno titán. Percy fracasa en un primer intento de detener en alta mar las arrolladoras huestes de Cronos e, inevitablemente, estalla la contienda más sanguinaria y espeluznante de todos los tiempos, un auténtico enfrentamiento por la supervivencia. Los olímpicos se esfuerzan en mantener a raya la furia desatada del monstruo Tifón. Cronos ordena el avance definitivo hacia la ciudad de Nueva York, donde el monte Olimpo, en lo alto del Empire State, se encuentra prácticamente indefenso. Pararle los pies al implacable Señor del Tiempo dependerá exclusivamente de Percy Jackson y un pequeño ejército de jóvenes semidioses... En esta última y trascendental entrega de la serie, la profecía largamente anunciada en torno al decimosexto cumpleaños de Percy se hace por fin realidad. Y mientras la batalla por la civilización occidental se libra con brutal ensañamiento en las calles de Manhattan, Percy abriga la terrible sospecha de estar luchando tal vez contra su propio destino.'];
var links=new Array(
    'res/El ladron del rayo - Rick Riordan.epub',
    'res/El mar de los monstruos - Rick Riordan.epub',
    'res/La maldicion del Titan - Rick Riordan.epub',
    'res/La batalla del laberinto - Rick Riordan.epub',
    'res/El ultimo heroe del Olimpo - Rick Riordan.epub');
var idLibro = new Array[0,1,2,3,4];
$(document).ready(function(){
    $('ul.tabs').tabs();
});
$(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();    
});
function construirDiv(array){
    for ( var i = 0, l = array.length; i < l; i++ ) {
        var meter= "<div class='vistPrev' onclick='cambiarPortada("+array[i]+")'><img src="+img[array[i]]+" width='100%' height='100%' img></div>"; 
        $("#librosPorLetra").append(meter);
    }
    meter="<div id='elModal' class='modal modal-fixed-footer' style='display: none; opacity: 1; top: 10%;'><div class='modal-content'><div style='width:20%; position:fixed; margin-left:72%'><img id='modalI' src='img/percy1.jpg' width='100%' height='30%' img></div><div class='vistPrev' style='width:75%'><h4 id='modalH'>Modal Header</h4><p id='modalP'></p></div></div><div class='modal-footer'><a href='#!' class='modal-action modal-close waves-effect waves-red btn-flat '>Cerrar</a><a id='modalMI' href='#!' class='modal-action modal-close waves-effect waves-green btn-flat '>Descargar</a></div></div>";
    $("#librosPorLetra").append(meter);
}
function cambiarLetra(letra){
    $("#librosPorLetra").empty();
    var librosLetrados= [];
    if (letra=="#"){
    }else{
        for( var i = 0, l = idLibro.length; i < l; i++ ) {
            if (titulos[idLibro[i]].charAt(0)==letra || titulos[idLibro[i]].charAt(0)==letra.toUpperCase()){
                librosLetrados.push(idLibro[i]);
            }
        }
        construirDiv(librosLetrados);
    }
}

function activar(elemento){
    switch(elementoAnterior){
        case 1:
            $("#id1").removeClass("active");
            break;
        case 2:
            $("#id2").removeClass("active");
            break;
        case 3:
            $("#id3").removeClass("active");
            break;
        default:
            console.log("Error");
    }
    elementoAnterior=elemento;
    switch(elemento){
        case 1:
            $("#id1").addClass("active");
            break;
        case 2:
            $("#id2").addClass("active");
            break;
        case 3:
            $("#id3").addClass("active");
            break;
        default:
            console.log("Error");
    }
}
function cambiarPortada(tocado){
    $('#elModal').openModal();
    $("#modalI").attr('src', img[tocado]);
    $("#modalH").html(titulos[tocado]);
    $("#modalP").html(contenido[tocado]);
    $("#modalMI").attr('href', links[tocado]);
}