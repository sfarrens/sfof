#!/usr/bin/env python

import argparse
import subprocess
import datetime
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
     
    t = datetime.datetime.now()
    ts = t.isoformat().replace(':','')
    out_clusters = 'EUC-TEST-LE3COGCLUS-%s.fits' % ts
    out_members  = 'EUC-TEST-LE3COGMEMB-%s.fits' % ts  
    
    t_opt['output_clusters'] = 'data/%s' % out_clusters
    t_opt['output_members' ] = 'data/%s' % out_members   
  
    conf=["euclid.le3.cog.fof_cluser_finder"]
    

    for (o,v) in t_opt.items():
        conf.append('--'+o)
        conf.append(v)
        print ('--%s %s' % (o,v))
        
        
#    proc = subprocess.Popen(conf, stdout = subprocess.PIPE, \
#    stderr = subprocess.PIPE, shell = True, close_fds = True)
#    (stdoutdata, stderrdata) = proc.communicate()

        
    proc = subprocess.Popen(conf)
    proc.wait()
    
    r_code = proc.returncode
    if r_code != 0:
        exit(r_code)
    
    dm_o = gal.GalClusterOutput()
    dm_o.Clusters = gal.pyxb.BIND(version='0.1')
    #pyxb complains about fixed attributes even if it correctly populates it...
    dm_o.Clusters.format = dm_o.Clusters.format
    dm_o.Clusters.DataContainer = gal.pyxb.BIND(filestatus='PROPOSED')
    dm_o.Clusters.DataContainer.FileName = gal.pyxb.BIND(out_clusters)
    
    dm_o.Members = gal.pyxb.BIND(version='0.1')
    #same consideration
    dm_o.Members.format = dm_o.Members.format
    dm_o.Members.DataContainer = gal.pyxb.BIND(filestatus='PROPOSED')
    dm_o.Members.DataContainer.FileName = gal.pyxb.BIND(out_members)   

    with open(args.output,'w+t') as f:
        f.write(dm_o.toxml())
        
#     --input_file test_phot.dat --input_mode ascii --output_mode ascii --link_r 0.86 --link_z 1.0 --min_ngal 3 --kdtree_depth 7