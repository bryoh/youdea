'use strict'
var supportsAudio = !! document.createElement('audio').canPlayType;
if (supportsAudio) {
    var player = new Plyr('#audio', { 
        controls: [
            'rewind',
            'play',
            'progress',
            'current-time',
            'duration',
            'fast-forward',
            'download',
        ]
    });
    $( document ).ready(function() {
        console.log( "ready!" );
        $('.clickable-row')[0].click();
    });
    var currentTrack = 0,
        playing = false,
        npAction = $('#npAction'),
        npTitle = $('#npTitle'),
        audio = $('#audio').on('play', function() {
            playing = true;
            var current_song = $('.clickable-row.table-active td')[1];
            npAction.text(current_song.textContent);
        }).on('pause', function() {
            playing = false;
            npAction.text('Paused...')
        }).on('ended', function() {
            playing = false;
            npAction.text('Paused...')
        }).get(0),
        row = $('.clickable-row').click(function (){
            $('.clickable-row.table-active').removeClass('table-active')
            var fileurl = $(this).attr('data-href');
            $(this).addClass('table-active');
            audio.src = fileurl; 
            //alert(fileurl);
            player.on('loadedmetadata', function() {
                $('a[data-plyr="download"]').attr('href', fileurl);
            });
            audio.play();
        })


} else {
    // no audio suppport
    var noSupport = 'No support'
}

