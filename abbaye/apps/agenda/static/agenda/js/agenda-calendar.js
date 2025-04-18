$(document).ready(function () {
  url = new URL(window.location);

  // Lier le datepicker à l'input date :
  $(function () {
    var values = {
      dateFormat: "dd/mm/yy",
      minDate: null,
      dayNames: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
      dayNamesMin: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
      monthNames: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
      monthNamesShort: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"],
      onSelect: function () {
        var path = url['origin'] + '/abbaye/agenda/calendar/';
        window.location.replace(path + $(this).val().split("/").reverse().join("-"));
      },
    }
    $("#datepicker").datepicker(values);
  });

  // Details: fill modal when clicked on a bar:
  $('#calendar')
    .on(
      'click',
      '.event_bar',
      function () {
        const id = $(this).attr('id').split('_')[1];
        $.get('/abbaye/agenda/' + id, function (data) {
          $('.modal-content').html(data);
        });
      }
    ).on(
      'click',
      '.absence_bar',
      function () {
        const id = $(this).attr('id').split('_')[1];
        $.get('/abbaye/absences/' + id, function (data) {
          $('.modal-content').html(data);
        });
      }
    ).on(
      'click',
      '.presence_bar',
      function () {
        const id = $(this).attr('id').split('_')[1];
        $.get('/abbaye/absences/' + id, function (data) {
          $('.modal-content').html(data);
        });
      }
    )
});
