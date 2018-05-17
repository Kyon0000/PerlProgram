#!/usr/bin/perl

$string = “Your IP Address is”. $ENV{‘REMOTE_ADDR’};

print ‘Content-Type: text/html’. “¥r¥n¥r¥n”;
print ‘<html>’;
print ‘<head>’;
print ‘<title>This is CGI Test.</test>;
print ‘</head>;
print ‘<body>’;

print ‘<p>$string</p>’;

print ‘</body>’;
print ‘</html>;