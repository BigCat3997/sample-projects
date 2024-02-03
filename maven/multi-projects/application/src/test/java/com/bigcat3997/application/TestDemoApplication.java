package com.bigcat3997.application;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class TestDemoApplication {

	@Test
	public void testAdd() {
		assertEquals(42, Integer.sum(19, 23));
	}
}
