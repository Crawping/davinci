/*
 * This file is part of the DOM implementation for KDE.
 *
 * Copyright (C) 1999 Lars Knoll (knoll@kde.org)
 *           (C) 1999 Antti Koivisto (koivisto@kde.org)
 *           (C) 2001 Dirk Mueller (mueller@kde.org)
 * Copyright (C) 2004 Apple Computer, Inc.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public License
 * along with this library; see the file COPYING.LIB.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 *
 */
#ifndef NameNodeList_h
#define NameNodeList_h

#include "NodeList.h"
#include "PlatformString.h"

namespace WebCore {

/**
 * NodeList which lists all Nodes in a Element with a given "name=" tag
 */
class NameNodeList : public NodeList {
public:
    NameNodeList(Node* doc, const String& name);

    // DOM methods overridden from  parent classes

    virtual unsigned length() const;
    virtual Node* item(unsigned index) const;

    // Other methods (not part of DOM)
    virtual void rootNodeAttributeChanged() { NodeList::rootNodeChildrenChanged(); }

protected:
    virtual bool nodeMatches(Node* testNode) const;

    String nodeName;
};

} // namespace WebCore

#endif // NameNodeList_h