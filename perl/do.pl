#!/usr/bin/perl -w

use strict;
use utf8;
use Carp;
use Clone qw(clone);

use Cwd qw(abs_path);
use File::Basename;
use File::Spec;
use Getopt::Long qw(:config auto_help);
use Data::Dumper;

use lib abs_path(dirname(__FILE__)) . ""; #use current folder as lib
#for (@INC) {print "$_/\n";};
use PU;

my %OPTIONS = ();
GetOptions(
    \%OPTIONS,
    qw/player_id=s  times file=s/
);
my $DEFAULT_BENCHMARK_TIMES = 100;

main();

sub main {
    #benchmark(\&benchmark1, \&benchmark2, $DEFAULT_BENCHMARK_TIMES);
    #read_from_std_in();
    #print_array(get_all_sub_names(__FILE__));
    my $yaml = load_yaml('database.yaml');
    print_pretty_json($yaml);
    #print $data_json, "\n";
}

sub benchmark1 {
    print "xxx\n";
}

sub benchmark2 {
    print "xxx\n";
}