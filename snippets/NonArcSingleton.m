#import "NonArcSingleton.h"

static NonArcSingleton *sharedInstance = nil;

@implementation NonArcSingleton

@synthesize someProperty;

#pragma mark Singleton Methods

+ (instancetype)sharedInstance {
  static dispatch_once_t pred = 0;
  dispatch_once(&pred, ^{
    sharedInstance = [[self alloc] init]; // or some other init method
  });
  return sharedInstance;
}


- (instancetype)copyWithZone:(NSZone *)zone {
  return self;
}


- (instancetype)retain {
  return self;
}


- (NSUInteger)retainCount {
  return UINT_MAX; //denotes an object that cannot be released
}


- (oneway void)release {
  // never release
}


- (instancetype)autorelease {
  return self;
}


- (instancetype)init {
  if (self = [super init]) {
      self.someProperty = [[NSString alloc] initWithString:@"Default Property Value"];
  }
  return self;
}


- (void)dealloc {
  // Should never be called, but just here for clarity really.
  [someProperty release];
  [super dealloc];
}

@end
