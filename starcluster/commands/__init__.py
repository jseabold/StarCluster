# Copyright 2009-2014 Justin Riley
#
# This file is part of StarCluster.
#
# StarCluster is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# StarCluster is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with StarCluster. If not, see <http://www.gnu.org/licenses/>.

from starcluster.commands.start import CmdStart
from starcluster.commands.addnode import CmdAddNode
from starcluster.commands.removenode import CmdRemoveNode
from starcluster.commands.stop import CmdStop
from starcluster.commands.terminate import CmdTerminate
from starcluster.commands.restart import CmdRestart
from starcluster.commands.sshmaster import CmdSshMaster
from starcluster.commands.sshnode import CmdSshNode
from starcluster.commands.sshinstance import CmdSshInstance
from starcluster.commands.listclusters import CmdListClusters
from starcluster.commands.s3image import CmdS3Image
from starcluster.commands.ebsimage import CmdEbsImage
from starcluster.commands.downloadimage import CmdDownloadImage
from starcluster.commands.createvolume import CmdCreateVolume
from starcluster.commands.resizevolume import CmdResizeVolume
from starcluster.commands.listkeypairs import CmdListKeyPairs
from starcluster.commands.listzones import CmdListZones
from starcluster.commands.listregions import CmdListRegions
from starcluster.commands.listimages import CmdListImages
from starcluster.commands.listbuckets import CmdListBuckets
from starcluster.commands.showimage import CmdShowImage
from starcluster.commands.showbucket import CmdShowBucket
from starcluster.commands.removevolume import CmdRemoveVolume
from starcluster.commands.removeimage import CmdRemoveImage
from starcluster.commands.listinstances import CmdListInstances
from starcluster.commands.listspots import CmdListSpots
from starcluster.commands.showconsole import CmdShowConsole
from starcluster.commands.listvolumes import CmdListVolumes
from starcluster.commands.listpublic import CmdListPublic
from starcluster.commands.runplugin import CmdRunPlugin
from starcluster.commands.spothistory import CmdSpotHistory
from starcluster.commands.loadbalance import CmdLoadBalance
from starcluster.commands.shell import CmdShell
from starcluster.commands.createkey import CmdCreateKey
from starcluster.commands.removekey import CmdRemoveKey
from starcluster.commands.put import CmdPut
from starcluster.commands.get import CmdGet
from starcluster.commands.help import CmdHelp

all_cmds = [
    CmdStart(),
    CmdStop(),
    CmdTerminate(),
    CmdRestart(),
    CmdListClusters(),
    CmdSshMaster(),
    CmdSshNode(),
    CmdPut(),
    CmdGet(),
    CmdAddNode(),
    CmdRemoveNode(),
    CmdLoadBalance(),
    CmdSshInstance(),
    CmdListInstances(),
    CmdListSpots(),
    CmdListImages(),
    CmdListPublic(),
    CmdListKeyPairs(),
    CmdCreateKey(),
    CmdRemoveKey(),
    CmdS3Image(),
    CmdEbsImage(),
    CmdShowImage(),
    CmdDownloadImage(),
    CmdRemoveImage(),
    CmdCreateVolume(),
    CmdListVolumes(),
    CmdResizeVolume(),
    CmdRemoveVolume(),
    CmdSpotHistory(),
    CmdShowConsole(),
    CmdListRegions(),
    CmdListZones(),
    CmdListBuckets(),
    CmdShowBucket(),
    CmdRunPlugin(),
    CmdShell(),
    CmdHelp(),
]
