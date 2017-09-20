package PU;
use strict;
use warnings;
our @ISA = qw(Exporter);
our @EXPORT_OK = qw/sort/;
our $sub_names = get_all_sub_names(__FILE__);
our @EXPORT = @$sub_names;
#print_list($sub_names);

use Benchmark;
use YAML::Syck;
use JSON::XS;

#
sub read_from_file {
    my ($file) = @_;
    my @data = ();
    if (!defined($file)) {
        return \@data;
    }

    open FIN, $file or die 'Cannot open ' . $file . '. Error: ' . $!;
    @data = <FIN>;
    return \@data;
}

sub load_yaml {
    my ($file) = @_;
    my $yaml = YAML::Syck::LoadFile($file);
}

sub convert_to_json {
    my ($data_ref) = @_;
    my $json_text = JSON::XS->new->utf8->allow_nonref->encode ($data_ref);
    return $json_text;
}

sub convert_to_pretty_json {
    my ($data_ref) = @_;
    my $json_text = JSON::XS->new->utf8->allow_nonref->pretty->encode ($data_ref);
    return $json_text;
}

sub print_pretty_json {
    my ($data_ref) = @_;
    my $json_text = JSON::XS->new->utf8->allow_nonref->pretty->encode ($data_ref);
    print $json_text, "\n";
}

sub print_list {
    my ($arr_ref) = @_;
    my $i = 0;
    for (@$arr_ref) {
        print "$i: $_\n";
        $i++;
    }
}

# Read user's input from standard until type 'end';
# @return a list ref
sub read_from_std_in {
    my @data = ();
    while (<STDIN>) {
        chomp $_; #Ignore new line character
        if ($_ =~ /^end$/) {
            last;
        }
        push @data, $_;
    }

    return \@data;
}

#hack: supposed that sub name is on single line
#@return a list contains all function name
sub get_all_sub_names {
    my ($file) = @_;
    my $text = read_from_file($file);
    my @sub_names = ();
    for (@$text) {
        #print "$1\n" if m/^sub\s+(\w+)\s?+\{$/;
        push @sub_names, $1 if m/^sub\s+(\w+)/;
    }

    return \@sub_names;
}

#@param sub1, sub2: subrountine ref
sub benchmark {
    my ($sub1, $sub2, $times) = @_;
    if (ref $sub1 ne 'CODE' || ref $sub2 ne 'CODE') {
        die 'Sub1 and Sub2 must be sub ref';
    }
    $times = defined $times ? $times : 100;
    timethese($times, +{sub1 => $sub1, sub2 => $sub2});
}

1