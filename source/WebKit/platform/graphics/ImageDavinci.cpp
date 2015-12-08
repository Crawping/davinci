/*
 * ImageDavinci.h: Image implements by davinci.
 *
 * Copyright(C) 2015 Zhang Ji Peng (onecoolx@gmail.com)
 *
 */

#include "config.h"
#include "Image.h"

namespace WebCore {

void Image::drawPattern(GraphicsContext*, const FloatRect& srcRect, const AffineTransform& patternTransform,
        const FloatPoint& phase, ColorSpace styleColorSpace, CompositeOperator, const FloatRect& destRect, BlendMode)
{
}

PassRefPtr<Image> Image::loadPlatformResource(const char* name)
{
}

}
