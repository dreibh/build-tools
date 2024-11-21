# System-Tools
# Copyright (C) 2013-2025 by Thomas Dreibholz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact: thomas.dreibholz@gmail.com


#############################################################################
#### PROGRAMS                                                            ####
#############################################################################

INSTALL(PROGRAMS    build-tool   DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES       build-tool.1 DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)
INSTALL(FILES       build-tool.bash-completion
        DESTINATION ${CMAKE_INSTALL_DATADIR}/bash-completion/completions
        RENAME      build-tool)

INSTALL(PROGRAMS version-bump DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES version-bump.1  DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)
INSTALL(FILES       version-bump.bash-completion
        DESTINATION ${CMAKE_INSTALL_DATADIR}/bash-completion/completions
        RENAME      version-bump)


#############################################################################
#### CONFIGURATION FILES                                                 ####
#############################################################################

INSTALL(FILES pbuilderrc DESTINATION ${CMAKE_INSTALL_DATADIR}/build-tools)


#############################################################################
#### EXAMPLES                                                            ####
#############################################################################
