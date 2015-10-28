var gulp = require('gulp');
var react = require('gulp-react');
var esperanto = require('gulp-esperanto');
var path = require('path')
var sass = require('gulp-sass')
var concat = require('gulp-concat');

var reactifyAndTranspile = function(path, to) {
    return gulp.src(path)
        .pipe(react({es6module: true}))
        .pipe(esperanto({type: "amd"}))
        .pipe(gulp.dest(to));
}

gulp.task('default', function() {
    gulp.src('js/config.js').pipe(gulp.dest('static/js'));
    return reactifyAndTranspile(['js/**/*.js','!js/config.js'], 'static/js')
});

gulp.task('sass', function() {
    return gulp.src('scss/*.scss')
        .pipe(sass())
        .pipe(concat('main.css'))
        .pipe(gulp.dest('static/css'));
});

gulp.task('watch', function(){
    console.log("Rebuilding everything");
    reactifyAndTranspile(['js/**/*.js','!js/config.js'], 'static/js');
    gulp.src('js/config.js').pipe(gulp.dest('static/js'));
	gulp.watch('js/**/*.js', function(evt) {
        if (evt.path.lastIndexOf('config.js') == -1) {
            var jsFolder = path.resolve(__dirname, 'js')
            var relativePath = path.relative(jsFolder, evt.path);
            console.log(relativePath + " " + evt.type + ". Rebuilding...");
            try{
                reactifyAndTranspile(evt.path, path.resolve('static/js', path.dirname(relativePath)));
            } catch (err) {
                console.log("Error while rebuilding " + relativePath);
                console.log(err)
            }
        } else {
            gulp.src(evt.path).pipe(gulp.dest('static/js'));
        }
	});
    gulp.watch('scss/*.scss', ['sass']);
});