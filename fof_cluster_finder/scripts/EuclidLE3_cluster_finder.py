#!/usr/bin/env python

import argparse
import subprocess
import sys
import pyxb.utils.domutils as domutils

import euclid.dm.Interfaces.pro.le3.cog_stub as gal

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute the fof cluster finder algorithm')
    parser.add_argument('--input',metavar='input',type=str, dest='input',
                        help='input XML file', required=True)
    parser.add_argument('--output',metavar='output',type=str, dest='output',
                        help='output XML file', required=True)
    parser.add_argument('--log',metavar='log',type=str, dest='log',
                        help='log path', required=False)

    args = parser.parse_args()
    
    with open(args.input,'r+t') as f:
        xml = f.read()
    
    doc = domutils.StringToDOM(xml)

    dm_i = gal.GalClusterInput.createFromDOM(doc.documentElement)
    
    doc_params = dm_i.Params.toDOM()
    t_opt = {}
    for node in doc_params.firstChild.childNodes:
        t_opt[node.tagName] = node.firstChild.nodeValue
        
    
    t_opt["input_mode"] = "fits"
    t_opt["output_mode"] = "fits"
    
    if dm_i.Catalog.PhotZcatalog is not None:
        t_opt["fof_mode"] = "phot"
        t_opt["input_file"] = "data/%s" % dm_i.Catalog.PhotZcatalog.DataContainer.FileName

    else:
        t_opt["fof_mode"] = "spec"
        t_opt["input_file"] = "data/%s" % dm_i.Catalog.SpecZcatalog.DataContainer.FileName
            
  
    conf=["euclid.le3.galcluster.fof_cluser_finder"]
    

    for (o,v) in t_opt.items():
        conf.append('--'+o)
        conf.append(v)
        
    print (conf)
    
#    proc = subprocess.Popen(conf, stdout = subprocess.PIPE, \
#    stderr = subprocess.PIPE, shell = True, close_fds = True)
#    (stdoutdata, stderrdata) = proc.communicate()

        
    proc = subprocess.Popen(conf)
    proc.wait() 
    
#     --input_file test_phot.dat --input_mode ascii --output_mode ascii --link_r 0.86 --link_z 1.0 --min_ngal 3 --kdtree_depth 7