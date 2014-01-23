#import "ArcSingleton.h"

static ArcSingleton *sharedInstance = nil;

@implementation ArcSingleton

@synthesize someProperty;

#pragma mark Singleton Methods

+ (instancetype)sharedInstance {
  static dispatch_once_t pred = 0;
  __strong static id _sharedObject = nil;
  dispatch_once(&pred, ^{
    _sharedObject = [[self alloc] init]; // or some other init method
  });
  return _sharedObject;
}


- (instancetype)copyWithZone:(NSZone *)zone {
  return self;
}

- (instancetype)init {
  if (self = [super init]) {
      someProperty = [[NSString alloc] initWithString:@"Default Property Value"];
  }
  return self;
}


- (void)dealloc {
  // Should never be called, but just here for clarity really.
}

@end
